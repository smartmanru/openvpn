import unittest

from setup_ssh import SSHConfig


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(-9999, 9999)
        self.e = False
        self.port_range_min = 2200
        self.port_range_max = 2299
        self.port_range = range(self.port_range_min, self.port_range_max)

    def test_port_not_number(self):
        self.assertRaises(Exception, SSHConfig.__init__, "-p")
        self.assertRaises(Exception, SSHConfig.__init__, "-p abc")
        self.assertRaises(Exception, SSHConfig.__init__, "-p 123ABC")

    def test_port_not_in_range(self):
        for val in [x for x in self.seq if x not in self.port_range]:
            self.assertRaises(Exception, SSHConfig.__init__, "-p {0}".format(val),
                              self.port_range_min, self.port_range_max)

    def test_port_in_range(self):
        for val in self.port_range:
            self.assertIsNotNone(SSHConfig("-p {0}".format(val),
                                           self.port_range_min, self.port_range_max))

    def test_username(self):
        self.assertRaises(Exception, SSHConfig.__init__, "-u")
        self.assertRaises(Exception, SSHConfig.__init__, "-u Ivan Petrov")
        self.assertRaises(Exception, SSHConfig.__init__, "-u root")
        self.assertRaises(Exception, SSHConfig.__init__, "-u Root")
        self.assertRaises(Exception, SSHConfig.__init__, "-u -Incorrect")
        self.assertRaises(Exception, SSHConfig.__init__, "-u Incorrect -username")
        self.assertIsNotNone(SSHConfig("-u correct-username"))
        self.assertIsNotNone(SSHConfig("-u   correctusername  "))


if __name__ == '__main__':
    unittest.main()

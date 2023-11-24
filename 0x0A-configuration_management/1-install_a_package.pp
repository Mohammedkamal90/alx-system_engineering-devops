#!/usr/bin/pup
# Install a package flask

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

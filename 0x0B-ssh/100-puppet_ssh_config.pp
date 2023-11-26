#!/usr/bin/env bash
# Puppet manifest to configure SSH client

file { '/etc/ssh/ssh_config':
  ensure => present,
}

file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/ssh_config',
  match => '^#passwordAuthentication',
  line  => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  match => '^#IdentityFile',
  line  => 'IdentityFile ~/.ssh/school',
}

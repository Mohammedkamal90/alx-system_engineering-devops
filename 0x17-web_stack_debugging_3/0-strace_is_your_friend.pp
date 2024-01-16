# Ensure the required directory exists
file { '/var/www/html':
  ensure => directory,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0755',
}

# Your other configurations or resources can go here

# Notify Apache to reload its configuration
service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => File['/var/www/html'],  # Ensure the directory is created before restarting Apache
  notify  => Service['apache2'],
}

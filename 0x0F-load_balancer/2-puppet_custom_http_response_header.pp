# Install Nginx package
  package { 'nginx':
  ensure => installed,
}

# Get the server's hostname
$hostname = $facts['hostname']

# Configure Nginx with the custom header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Service definition for Nginx
  service { 'nginx':
  ensure  => running,
  enable  => true,
}

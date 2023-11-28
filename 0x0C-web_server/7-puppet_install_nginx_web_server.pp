#!/usr/bin/env bash
# Install Nginx
class nginx_server{
package { 'nginx':
  ensure => installed,
}

# Create basic HTML page with "Hello World!"
file { '/usr/share/nginx/html/index.html':
  ensure => present,
  content => 'Hello World!',
}

# Create configuration for redirect
file { '/etc/nginx/sites-available/redirect_me':
  ensure => present,
  content => 'location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
              }',
}

# Create symbolic link to enable the new site
file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => link,
  target => '/etc/nginx/sites-available/redirect_me',
}
}
# Restart Nginx to apply the changes
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => [File['/etc/nginx/sites-available/redirect_me'], File['/usr/share/nginx/html/index.html']],
}

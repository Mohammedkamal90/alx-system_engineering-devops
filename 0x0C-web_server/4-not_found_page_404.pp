#!/usr/bin/env bash
# Create custom 404 HTML page
file { '/usr/share/nginx/html/404.html':
  ensure => present,
  content => '<!DOCTYPE html><html><head><title>404 Not Found</title></head><body><p>Ceci n\'est pas une page</p></body></html>',
}

# Create configuration for custom error page
file { '/etc/nginx/sites-available/custom_404':
  ensure => present,
  content => 'error_page 404 /404.html;
              location = /404.html {
                root /usr/share/nginx/html;
                internal;
              }',
}

# Create symbolic link to enable the new site
file { '/etc/nginx/sites-enabled/custom_404':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_404',
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure => 'running',
  enable => 'true',
  require => [File['/etc/nginx/sites-available/custom_404'], File['/usr/share/nginx/html/404.html']],
}

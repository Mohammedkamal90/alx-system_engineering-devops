# increas amount of traffic Nginx server can handle
# increas ULIMIT default file

exec { 'fix-for-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
}

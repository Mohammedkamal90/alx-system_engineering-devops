# Execute_a_command

exec { 'killmenow':
  command => 'pkill -f killmenow',
  provider=> 'shell',
}

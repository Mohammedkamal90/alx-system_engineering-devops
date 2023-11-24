# Execute_a_command

exec { 'pkill':
  command => 'pkill -f killmenow',
  provider=> 'shell',
}

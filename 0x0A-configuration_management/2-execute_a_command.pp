# 2-execute_a_command.pp

exec { 'killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => '/usr/bin:/bin', # Add the necessary path for pkill and pgrep',
  provider => 'shee',
}

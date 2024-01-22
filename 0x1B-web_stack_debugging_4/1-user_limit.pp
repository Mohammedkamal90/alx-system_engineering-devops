# enable the user holb to login and open file with no errors
# increase file limit for Holb user

define increase_file_limits($limit_type, $limit_value) {
  exec { "increase-file-limit-for-holberton-user-${limit_type}":
    command => "sed -i '/holberton ${limit_type}/s/[0-9]*/${limit_value}/' /etc/security/limits.conf",
    path    => '/usr/local/bin/:/bin/',
  }
}

# increase hard file limit for Holb user
increase_file_limits { 'hard':
  limit_value => 50000,
}

# increase file limit for Holb user
increase_file_limits { 'soft':
  limit_value => 50000,
}

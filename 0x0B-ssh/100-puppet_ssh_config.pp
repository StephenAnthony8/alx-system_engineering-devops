# ssh config via puppet

file { '/home/your_username/.ssh':
  ensure  => directory,
  mode    => '0700',
  require => File['/home/your_username'],
}

file { '/home/your_username/.ssh/config':
  ensure  => present,
  content => "Host ubuntu@54.144.150.154\n" \
    "    PasswordAuthentication no\n" \
    "    HostName 54.144.150.153\n" \
    "    IdentityFile ~/.ssh/school\n",
  mode    => '0600',
  require => File['/home/your_username/.ssh'],
}

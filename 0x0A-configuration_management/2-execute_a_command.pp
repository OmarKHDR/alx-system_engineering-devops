# -=  =- 

exec{'kill_me':
    command   => 'pkill killmenow'
    provider  => 'shell'
}
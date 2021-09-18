# Fatal error: Allowed memory size of 1610612736 bytes exhausted but already allocated 1.75G
```bash
php -d memory_limit=-1 /usr/local/bin/composer install
```

## Cause: 
It will set memory_limit=-1 for XAMPP. Since there was an existing memory defined and which was exhausted

## 1. Fatal error: Allowed memory size of 1610612736 bytes exhausted but already allocated 1.75G
```bash
php -d memory_limit=-1 /usr/local/bin/composer install
```

### Cause: 
It will set memory_limit=-1 for XAMPP. Since there was an existing memory defined and which was exhausted


## 2. Fatal error: Allowed memory size of 1610612736 bytes exhausted (tried to allocate 4096 bytes) in phar:///usr/local/Cellar/composer/1.7.2/bin/composer/src/Composer/DependencyResolver/Solver.php on line 220

* Upgrade the composer version to composer2
```bash
#Remove Your older version: 
sudo rm -f /usr/local/bin/composer

#Download the installer: 
sudo curl -s https://getcomposer.org/installer | php

#Move the composer.phar file: 
sudo mv composer.phar /usr/local/bin/composer
```

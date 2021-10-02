# Install laravel from scratch and make it running on local server

This is a simple guide for installation of laravel 6 and make it a live project.

## Steps 

* Install Composer
* Create Laravel Project

## Getting Started

### Install Composer

* Run the following commands on terminal in order
```bash
# Download the installer to the current directory
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"

# Verify the installer SHA-384
php -r "if (hash_file('sha384', 'composer-setup.php') === '906a84df04cea2aa72f40b5f787e49f22d4c2f19492ac310e8cba5b96ac8b64115ac402c8cd292b8a03482574915d1a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

# Run the installer
php composer-setup.php

# Remove the installer
php -r "unlink('composer-setup.php');"
```

### Create Laravel Project

```bash
composer create-project --prefer-dist laravel/laravel myLaravel "6.*"
```

### Serve the project

* go to your project directory (In this case it is myLaravel)
```bash
cd myLaravel
```
* Serve the project
```php
php artisan serve
```

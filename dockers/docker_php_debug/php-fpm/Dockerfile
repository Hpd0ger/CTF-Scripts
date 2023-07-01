FROM php:7.2-fpm
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# multi-stage get composer
COPY --from=composer /usr/bin/composer /usr/bin/composer

COPY ./mongodb-1.14.1.tgz ./xdebug-3.1.5.tgz /tmp/

RUN pecl install /tmp/xdebug-3.1.5.tgz \
	&& docker-php-ext-enable xdebug

RUN set -xe \
    # 安装扩展
    && docker-php-ext-install -j$(nproc) pcntl \
    && docker-php-ext-install -j$(nproc) posix \
    && docker-php-ext-install -j$(nproc) pdo pdo_mysql \  
    && docker-php-ext-install -j$(nproc) mysqli

RUN apt-get update && apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libpng-dev \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini
COPY ./www.conf /usr/local/etc/php-fpm.d/www.conf
RUN cp /usr/local/etc/php/php.ini-development /usr/local/etc/php/php.ini

RUN usermod -u 1000 www-data
RUN chown -R www-data:www-data /var/www/html

ARG APP_CODE_PATH

WORKDIR ${APP_CODE_PATH}

CMD php-fpm

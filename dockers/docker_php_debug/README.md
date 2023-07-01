PHP Docker开发环境，PHPStorm及Xdebug的使用。

# 目录结构
| 文件夹名称 | 作用 |
|---|---|
| logs | 存放nginx&xdebug日志 |
| mysql | mysql-docker构建 |
| nginx | nginx构建 |
| php-fpm | php-fpm构建 |
| source | web源码 |
| .env | 控制docker-compose变量 |

# 说明
* 构建的web目录根路径在：/usr/share/nginx/html
* xdebug3.x，指定client_host为docker宿主机，端口为宿主机9003
* 默认nginx_host为localhost，通过.env更改


# 启动
```shell
cd docker
docker-compose up -d 
```



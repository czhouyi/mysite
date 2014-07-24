#kill cgi and nginx processes
ps -ef|grep python|grep -v grep|cut -c 9-15|xargs kill -9
ps -ef|grep nginx|grep -v grep|cut -c 9-15|xargs kill -9

#run cgi and nginx
python manage.py runfcgi host=192.168.188.128 port=8080
/usr/local/nginx/sbin/nginx

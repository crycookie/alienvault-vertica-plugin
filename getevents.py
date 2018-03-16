import vconfig
import vertica_python
import re

conn_inf = vconfig.conn_info
with vertica_python.connect(**conn_inf) as connection:
    cur = connection.cursor()
    cur.execute('select login_timestamp, database_name, user_name, client_hostname, client_pid, authentication_method, reason from login_failures where date(login_timestamp) = CURRENT_DATE-1 order by login_timestamp DESC;')
    check = cur.fetchall()
    last_db = check[0]
    with open('/var/log/vertica.log','r') as f:
        last_file = f.readlines()[-1].decode()

    if str(last_db[0]) != str(re.match(r'^.*(?:\,\sdatabase_name\:\s)',last_file)):
        for x in check:
            with open('/var/log/vertica.log','a') as g:
                g.write('\n'+str(x[0])+', database_name: '+ str(x[1])+', user_name: '+ str(x[2])+', client_hostname: '+str(x[3])+', client_pid: '+ str(x[4]) +', authentication_method: ' + str(x[5])+ ', reason: '+str(x[6]))

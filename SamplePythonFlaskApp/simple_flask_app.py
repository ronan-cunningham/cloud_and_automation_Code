from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import os
import json

parser = reqparse.RequestParser()
parser.add_argument('host', type=str, required=True, action='append', 
                     help='Enter each host as a cli arg with -d')
parser.add_argument('key', type=str, required=True, 
                     help='Enter your key as a cli arg with -d')

app = Flask(__name__)
api = Api(app)
app.config['BUNDLE_ERRORS'] = True


def run_ansible(state, key, hosts):

    remote_user = 'ec2-user'
    remote_file = "/home/%s/.ssh/authorized_keys" %(remote_user)

    if len(hosts) == 1 :
       hosts = hosts[0] + ','
    else:
       hosts = ','.join(hosts)
       
    cmd  = 'export ANSIBLE_HOST_KEY_CHECKING=False && '
    cmd += 'ansible all -i %s -m lineinfile ' %(hosts)
    cmd += " -a \"path=%s state=%s line='%s'\"" %(remote_file,state,key)
    cmd += " -u %s"  %(remote_user)
                
    try:
        os.system(cmd)
        if state == 'present':
            msg = "Key added to hosts - Success"
        else:
            msg = "Key removed from hosts - Success"
    except:
        if state == 'absent':
            msg = "Unable to add key to hosts - Error - please try again"
        else:
            msg = "Unable to remove key from hosts - Error - please try again"
    return msg


class Keys(Resource):
    def put(self):
    
        args       = parser.parse_args()
        key        = args['key']
        hosts      = args['host']
        
        if request.path == '/add':
            state      = 'present'
        else:
            state      = 'absent'
            
        key = run_ansible(state, key, hosts)
        
        return key
        
api.add_resource(Keys, '/add', '/delete')

if __name__ == '__main__':
    app.run(host="0.0.0.0") 

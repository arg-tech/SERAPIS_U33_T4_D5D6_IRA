import cherrypy
import pproc
import json
p = pproc.Pproc()

class WebService(object):

   @cherrypy.expose
   @cherrypy.tools.json_out()
   @cherrypy.tools.json_in()
   def process(self):
      data = cherrypy.request.json
      d = data['string']
      output = p.run(d)
      return json.dumps(output)

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update({'server.socket_port': 8199})
    cherrypy.config.update(config)
    cherrypy.quickstart(WebService())

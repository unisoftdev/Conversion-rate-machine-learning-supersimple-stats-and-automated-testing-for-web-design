import tornado.ioloop, os
import tornado.web

#######################################################################
import global_variable #import the tested variable                    #
import test_conversion #import the module which performs the tests    #
#######################################################################

class MainHandler(tornado.web.RequestHandler):
    def get(self, matched_part=None):
        path = self.request.path
        referer = self.request.headers.get("Referer")
        path = path.replace("/", "").lower()
        if str(path) == "":
                                                                     ########################
            # here, we start our script when use the variable  ------------> this variable  #
            index = '<!DOCTYPE HTML><html><body><button style=color:"'+ global_variable.color +';width:100%;height:auto"></button>press me</body></html>'
                                                                     ########################           
            self.write(str(index))
        elif str(path) == "contact-us":
##############################################################
          # here, we start the script to make stats and choose
            if referer == "":                                #
                test_conversion.Start()                      #
##############################################################
            contact_us = '<!DOCTYPE HTML><html><body><h1>Contact Us</h1></body></html>'
            self.write(str(contact_us))
        else:
            self.set_status(404)
def make_app():
    return tornado.web.Application([
        (r"/(.*)", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()



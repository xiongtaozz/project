class ProxyMiddleware(object):

    def process_request(self, request, spider):
        # Set the location of the proxy
        request.meta['proxy']= "http://%s:%d"%('222.211.65.72', 8080)
 



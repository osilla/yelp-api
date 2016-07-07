import rauth
import time

def main():
      params = get_search_parameters()
      api_calls = []
      api_calls.append(get_results(params))
      #rate-limit yourself
      time.sleep(1.0)
      
   ##Do more processing   

def get_results(params):

   #Yelp api keys
   consumer_key = "Lw-2G0GRmJKnYGaz89rUDA"
   consumer_secret = "caFKWLiZ6XjDuw8cqIrvFywpxzQ"
   token = "Ef3RCaQaLSijFrS-c5XEIFN0PntCcghR"
   token_secret = "whrfeVQq9WRDbb7e_FuzPk8NnEQ"
   
   session = rauth.OAuth1Session(
      consumer_key = consumer_key
      ,consumer_secret = consumer_secret
      ,access_token = token
      ,access_token_secret = token_secret)
      
   request = session.get("http://api.yelp.com/v2/search",params=params)
   
   #Transforms the JSON API response into a Python dictionary
   data = request.json()
   session.close()
   
   print data
  
      
def get_search_parameters():
   params = {}
   params["location"] = "pensacola"
   params["term"] = "optometrists"
   params["limit"] = "1"

   return params

if __name__=="__main__":
   main()

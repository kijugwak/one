import wikipedia
while True:
  query = input("어떤게 궁금하신가요?")
  
  try:
      results = wikipedia.summary(query, sentences =1)
      print(results)
      
  except:
    print("오류다 이색히야")

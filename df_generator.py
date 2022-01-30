from pyspark.sql import DataFrame
def df_generator(rows:int = 10) -> DataFrame:
  """
  The function that creates dummy dataframe with specified number of rows.
  
  Args:
  rows (int): number of rows in the dataframe 
    
  Returns:
  Dummy dataframe with two columns: "Name","Value"
  
  Examples:
  df_generator(10)
  df_generator(15)
  """
  assert type(rows) == int, f"Expected type is int, but found {type(rows)}"
  
  import requests
  import random
  #list of random numbers in range 1-1000
  lst = random.sample(range(1, 1000), rows)

  #get X random words based on length of numeric list
  word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
  response = requests.get(word_site)
  words_lst_init = [word.decode("utf-8") for word in response.content.splitlines()]
  words_lst = random.sample(words_lst_init, rows)

  #merging into tuples
  zippedlist = list(zip(words_lst, lst))

  df = spark.createDataFrame(zippedlist, "Name string, Value int")
  
  return df
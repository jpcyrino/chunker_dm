import regex


class Tokenizer():
    
  def __init__(self, text):
    self.texts = [text]
    self.tokens = self._tokenize(text)
    
  def _tokenize(self, text):
    return regex.sub(r"[^\p{L}\d\s]", "", text.lower()).split()  
    
  def add(self, text):
    self.texts.append(text)
    self.tokens.extend(self._tokenize(text))
    
  def getTokens(self):
    return self.tokens
    
    
    
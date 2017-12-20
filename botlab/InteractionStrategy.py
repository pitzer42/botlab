from botlab.nlp tokenize, tag

class InteractionStrategy:

    def reply(self, sender, message):
        tokens = tokenize(message)
        tagged_tokens = tag(tokens)
        answer = None
        feedback = 0
        try:
            answer = self._handle_tagged_tokens(tagged_tokens)

        except:
            answer = self.fallback()
        re

    def _handle_tagged_tokens
        pass

    def fallback():
        pass

    def feedback():
        pass

import string
ifile = """
        The birds have left their trees
        The light pours onto me
        I can feel you lying there all on your own
        We got here the hard way
        All those words that we exchange
        Is it any wonder things get broke?
        'Cause in my heart and in my head
        I'll never take back the things I said
        So high above, I feel it coming down
        She said, in my heart and in my head
        Tell me why this has to end
        Oh, no, oh, no
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
        Now all the birds have fled
        The hurt just leaves me scared
        Losing everything I've ever known
        It's all become too much
        Maybe I'm not built for love
        If I knew that I could reach you, I would go
        It's in my heart and in my head
        You can't take back the things you said
        So high above, I feel it coming down
        She said, in my heart and in my head
        Tell me why this has to end
        Oh, no, oh, no
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
        Yeah, we build it up and we build it up
        Yeah, we build it up to pull it down
        And we build it up and we build it up
        And we build it up to pull it down
        I can't save us, my Atlantis, we fall
        We built this town on shaky ground
        I can't save us, my Atlantis, oh, no
        We built it up to pull it down
"""


ifileNoPunc = ifile.translate(str.maketrans('','', string.punctuation))
ifileLowerCase = ifileNoPunc.lower()
ifileSplitted = ifileLowerCase.split()
ifileSplitted.sort()

print(ifileSplitted)
# Short and Sweet

Short and Sweet is an extractive text summarizer which incorporates Google's Word2Vec embeddings and a few linear algebra operations. The summarizer returns a non-repetitive, concise summary of a piece of text. Short and Sweet uses Flask to render the UI. 


## Results

Here is the text before summarization :

 

![Original](./docs/images/original.png) 

Here is the text after summarization :

 

![Summary](./docs/images/result2.png) 

## Installations and Downloads

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip3 install -r requirements.txt
```

This [link](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) contains the **word2vec pre-trained Google News corpus** (3 billion running words) word vector model (3 million 300-dimension English word vectors).

It is mirroring the data from the official word2vec website:
**GoogleNews-vectors-negative300.bin.gz**

Please download this file in the same folder as this project.

## Structure of the project
- The **try.py** file creates a dictionary from the model with words as key and vectors(300,) as values. Then this stores the dictionary using pickle. **Please note this new file consumes about 3.75 GB**.
You can delete the **GoogleNews-vectors-negative300.bin.gz** file after the **dictionary** file is made.

- The **backend.py** file contains the logic behind the summarizer. Please check out this file to understand the algorithm. This also includes all the linear algebra operations.

- The **templates** directory contains the **HTML** files used by the flask server.

- The **static** directory contains the **CSS** files used by the flask server.


## Usage


For the **first time only** 
run this in the terminal
```python
python3 try.py
```

Be patient as this may take a while to finish running (up to 10 minutes).
Then run the code below

**The second time onward run only this**
```python
python3 backend.py
```
Allow the model a few minutes (3-4) to load.

Open the browser and type http://localhost:5000/ in the url

The project is up and running! Enjoy and experiment!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)

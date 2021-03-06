
import setuptools
from distutils.core import setup

setup(
  name = 'easytoken',         
  packages = ['easytoken'],   
  version = '2.0.1',      
  license='MIT', 
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  description = 'easytoken is an independent Open Source, Natural Language Processing python library which implements a easytoken to create token from Both Sentence and Paragraph.',  
  author = 'Sayan Mondal(ph3n1x)',               
  author_email = 'sayanmondal2098@gmail.com',     
  url = 'https://github.com/sayanmondal2098/easytoken',   
  download_url = 'https://github.com/sayanmondal2098/easytoken',   
  keywords = ['NLP', 'Natural Language Processing', 'Tokenization', 'Text Summarization', 'Text Processing', 'Sentiment Analysis'],   # Keywords that define your package best
  install_requires=[         
          'nltk',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "1 - Planning" , "2 - Pre-Alpha"  "3 - Alpha", "4 - Beta" 
                                                        #    or "5 - Production/Stable", "6 - Mature", "7 - Inactive" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',# Again, pick a license
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)

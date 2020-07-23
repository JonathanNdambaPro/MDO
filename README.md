# MDO

MDO (Mahanalobis detection outliers) is a method based on the inference of some parameters (means vertors and precisions matrice) of gaussian mixture with the EM algorithm to define mahanalobis distance 
and a scoring.


[For more explanation]()
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install MDO.

```bash
pip install MDO
```

## Usage

```python
import MDO
params = { 
    n_components : 10,
    covariance_type : 'full',
    ...
    } #Parameters for bayesian Gaussian mixture or the usual one 

MDO.fit(X, inference_type='bayesian', **params) # Procede to inference for finding parameters (means and precision matrice)
List_scoring_local = MDO.get_scoring("local") # returns local scoring
List_scoring_global = MDO.get_scoring("global") # returns global scoring 
```


[Example of using](https://pip.pypa.io/en/stable/) 



## License
[MIT](https://choosealicense.com/licenses/mit/)
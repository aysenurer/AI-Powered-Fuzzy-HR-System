import pandas as pd 
import numpy as np 

np.random.seed(42) 
def generate_data(n=500):
    df = pd.DataFrame({
        "gpa": np.round(np.random.uniform(2.0, 4.0, n), 2), 
        "experience": np.random.randint(0, 11, n), 
        "projects": np.random.randint(0, 21, n), 
        "test_score": np.random.randint(30, 101, n), 
        "communication": np.random.randint(20, 101, n) 
        })
    
    df.to_csv("data/candidates.csv", index=False) 

    print("Dataset created!")

if __name__ == "__main__": 
    generate_data()
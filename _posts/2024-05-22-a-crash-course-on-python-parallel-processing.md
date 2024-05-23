---
layout: post
title:  "Crash Course on Python Parallel Processing"
date:   2024-05-22 21:25 +0530
categories: posts
---

You are in a company X where you want to run crash testing. every test is time consuming and you have only one python terminal at disposal.
let's setup the base code and run sequentially

<!--more-->

```python
class CrashTest:
    def __init__(self, car_cfg):
        self.car_cfg = car_cfg
        self.tests = []

    @timer
    def _run_test(self, crash_cfg):
        np.random.seed(10)
        sim_cplx = crash_cfg['simulation_complexity']
        car_cplx = self.car_cfg['mesh_complexity']
        crash_cfg['name'] = f'{crash_cfg["type"]}__{sim_cplx}__{car_cplx}'
        x = sim_cplx * car_cplx
        time.sleep(np.random.rand()*x/1000)
        o = {**crash_cfg, **self.car_cfg}
        return o

    def run_test(self, crash_cfg):
        o = self._run_test(crash_cfg)
        self.tests.append(o)
        return o

    def run_all_tests(self, crashes):
        for cfg in crashes:
            self.run_test(cfg)

    def change_mesh(self, complexity):
        self.car_cfg['mesh_complexity'] = complexity

    def __repr__(self):
        return 'Crash Tester'
```


```python
@timer
def main():
    crashes = [
        {'type': 'side', 'simulation_complexity': 10},
        {'type': 'front', 'simulation_complexity': 50},
        {'type': 'rear', 'simulation_complexity': 20}
    ]
    car = {'mesh_complexity':200}
    c = CrashTest(car)
    c.run_all_tests(crashes)
    c.change_mesh(complexity=400)
    c.run_all_tests(crashes)
    return {'tests': c.tests}

o = main()
duration = o['end'] - o['start']
print(f'{duration=} s')
```

    duration=37.05401233399971 s


<img src='https://i.imgur.com/RKNlZ7g.png' alt='image' style='max-height: 600px; width=auto;'>

As you can see the whole effort took 37 seconds. The program was executing one simulation after another. As you know computers have more CPUs and each CPU has multiple threads, which can pick up code and do computations parallely. Let's use python's threading to start as many new threads as required for each crash, during the function `run_all_tests`. During creation of each thread, we'll also get it rolling by calling `thread.start` and append it to a list of threads so that we can collect the results for all of them at once.


```python
import threading

class AsyncCrashTest(CrashTest):
    def run_all_tests(self, crashes):
        threads = []
        for crash in crashes:
            thread = threading.Thread(target=self.run_test, args=(crash,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
```


```python
@timer
def main():
    np.random.seed(10)
    crashes = [
        {'type': 'side', 'simulation_complexity': 10},
        {'type': 'front', 'simulation_complexity': 50},
        {'type': 'rear', 'simulation_complexity': 20}
    ]
    
    car = {'mesh_complexity':200}
    c = AsyncCrashTest(car)
    c.run_all_tests(crashes)
    
    c.change_mesh(complexity=400)
    c.run_all_tests(crashes)
    
    return {'tests': c.tests}

o = main()
duration = o['end'] - o['start']
print(f'{duration=} s')
```

    duration=23.14907920800033 s


![](https://i.imgur.com/K9c39bc.png)

Only 23s now. There's a significant drop in the total time taken! We can take it a step further and start all the threads for all the simulations at once, and gather all the results only at the end.


```python
import threading

class AsyncCrashTest(CrashTest):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.threads = []
        
    def run_all_tests(self, crashes):
        for crash in crashes:
            thread = threading.Thread(target=self.run_test, args=(crash,))
            thread.start()
            self.threads.append(thread)

    def get_all_results(self):
        for thread in self.threads:
            thread.join()
```


```python
@timer
def main():
    np.random.seed(10)
    crashes = [
        {'type': 'side', 'simulation_complexity': 10},
        {'type': 'front', 'simulation_complexity': 50},
        {'type': 'rear', 'simulation_complexity': 20}
    ]
    
    car = {'mesh_complexity':200}
    c = AsyncCrashTest(car)
    c.run_all_tests(crashes)
    
    c.change_mesh(complexity=400)
    c.run_all_tests(crashes)

    c.get_all_results()
    return {'tests': c.tests}

o = main()
duration = o['end'] - o['start']
print(f'{duration=} s')
```

    duration=15.4309698750003 s


![](https://i.imgur.com/0R1KKOw.png)

Only 15 seconds! As you can see, we used the power of parallel processing to start all the computations at once and collect them all at the end, without worrying about when each one of them completes. This makes the whole process quick and the only factor that decides the final time is the slowest simulation

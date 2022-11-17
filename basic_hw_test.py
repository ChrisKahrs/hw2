import gym
import highway_env
from matplotlib import pyplot as plt
# %matplotlib inline
import pyvirtualdisplay

display = pyvirtualdisplay.Display(visible=False, size=(1080, 920))
display.start()
env  = gym.make('CartPole-v1')
env.reset()
import matplotlib.pyplot as ply

img = plt.imshow(env.render('rgb_array'))
for _ in range(100):
    action = env.action_space.sample()
    curr_state, _, done, info = env.step(action) 

    display.clear_output(wait=True)
    img.set_data(env.render('rgb_array'))
    plt.axis('off')
    display.display(plt.gcf())

    if done:
        env.reset()
display.close()

# env = gym.make('highway-v0')
# env.reset()
# for _ in range(3):
#     action = env.action_type.actions_indexes["IDLE"]
#     obs, reward, done, truncated, info = env.step(action)
#     env.render()

# plt.imshow(env.render(mode="rgb_array"))
# plt.show()
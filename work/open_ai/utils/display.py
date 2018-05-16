#
# OpenAI Gym のシミュレーションを可視化
#
# ref: http://mckinziebrandon.me/TensorflowNotebooks/2016/12/21/openai.html
# ref: https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server

from matplotlib import animation
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'nbagg')
from IPython.display import display
from JSAnimation.IPython_display import display_animation

# 全フレームをまとめて再生
def display_frames_as_gif(frames):
    patch = plt.imshow(frames[0])
    plt.axis('off')

    def animate(i):
        patch.set_data(frames[i])

    anim = animation.FuncAnimation(plt.gcf(), animate, frames = len(frames), interval=50)
    display(display_animation(anim, default_mode='loop'))
    
# 1フレームずつ再生（重い）
def display_frame(env, step=0, info=""):
    plt.figure(3)
    plt.clf()
    plt.imshow(env.render(mode='rgb_array'))
    plt.title("%s | Step: %d %s" % (env.spec.id, step, info))
    plt.axis('off')

    display.clear_output(wait=True)
    display.display(plt.gcf())
    
#  display_frameで再生したディスプレイをクリアする
def clear_display():
    display.clear_output(wait=True)
    
"""
Draw a fireworks display!
"""

def setup():
    global bg, firework, fireworks_display, countdown
    
    # 1. Use the size(width, height) function to set the size of your program
    # to at least 1200 width, 800 height
    
    # 2. Use the loadImage() function to initialize the 'bg' variable
    # bg = loadImage('sanDiego.jpg')
    # bg = loadImage('futureCity.jpg')

    # 3. Use the bg variable's resize(width, height) to set the background image
    # to the size of your program
    
    # 4. Initialize the 'firework' variable to a Firework(x, y)
    # You can choose the values for x and y


def draw():
    global firework
    
    # 5. Call the image(bg, 0, 0) function to display your background  

    # 6. Call tint(255, 50)
    
    # 7. Call the firework variable's draw() method 
    # Do you see the firework when you run the program?
    
    # 8. Use an 'if' statement and the mousePressed variable to check if the
    # the mouse is pressed

        # 9. Set the 'firework' variable to a new Firework at mouseX and mouseY
        
        # EXTRA
        # Can you figure out how to:
        # * Make the fireworks sparkle?
        # * Make a multi-colored firework?
        # * Set the size of your firework?
        # * Play a sound when the firework explodes?

        #set_sound("arcade_explode2.mp3")
        # other sounds to choose from:
        #   arcade_explode1.mp3, arcade_explode2.mp3, arcade_explode3.mp3 
        #   arcade_bomb1.mp3, arcade_bomb2.mp3, arcade_bomb3.mp3
        #   airHorn1.mp3, airHorn2.mp3


















  # SUPER SECRET EXTRA
  # 1. Let's set up a fireworks display! Copy the following code at the end of the 
  # setup() method:
  #   fireworks_display = FireworksDisplay()
  #
  #    for i in range(10):
  #        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
  #        new_firework = Firework(random(width), random(height), colors[i % len(colors)])
  #        fireworks_display.add_firework(new_firework, i*1000)
  #    
  #    for k in range(30):
  #        colors = ['#FF0000', '#FFFFFF', '#0000FF']
  #        new_firework = Firework(random(width), random(height), colors[i % len(colors)])
  #        fireworks_display.add_firework(new_firework, (100*k) + 10000)
  #
  # 2. Create a Countdown object in the setup() method with a starting value of 10.
  # This will create a timer that counts down from 10 to 0.
  #
  # 3. Call the fireworks_display's launch() method and the Countdown object's draw() method.
  # How do the fireworks look? See if you can modify some of the code to make your
  # own unique New Year's fireworks celebration!


# =================== DO NOT MODIFY THE CODE BELOW ======================

class Firework:
    
    @staticmethod
    def get_random_color():
        return color(random(255), random(255), random(255))

    def __init__(self, x=None, y=None, firework_colors=None, sound=None):
        self.x = x
        self.y = y
        self.firework_colors = color(255) if firework_colors is None else firework_colors
        self.sound = sound
        self.sound_playing = False
        self.particles = list()
        self.particles_per_firework = 75
        
        # Default white firework
        for _ in range( self.particles_per_firework ):
            particle_color = self.firework_colors
            
            if isinstance(self.firework_colors, list):
                particle_color = self.firework_colors[int(random(len(self.firework_colors)))]
            
            particle = Particle(self.x, self.y, particle_color)
            self.particles.append(particle)

    def set_color(self, fw_color=None):        
        for particle in self.particles:
            particle.particle_color = fw_color

    def set_multi_colored_firework(self):
        for p in self.particles:
            p.particle_color = Firework.get_random_color();
  
    def set_size(self, min_size, max_size):
        for p in self.particles:
            p.particle_size = random(min_size, max_size)

    def set_sparkle(self, setting):
        for p in self.particles:
            p.is_sparkle = setting
            
    def set_sound(self, fw_sound):
        self.sound = fw_sound
  
    def draw(self):
        for p in self.particles:
            if self.sound is not None and not self.sound_playing:
                play_sound(self.sound)
                self.sound_playing = True
            p.update()
            p.draw()
    
        self.purge();

    def purge(self):
        self.particles[:] = [p for p in self.particles if p.new_y <= height]


class Particle:
    def __init__(self, x, y, particle_color=None, min_size=None, max_size=None):                  
        self.new_x = None
        self.old_x = None
        self.new_y = None
        self.old_y = None
        #self.dir = None
        #self.magnitude = None
        self.x_velocity = None
        self.y_velocity = None
        self.gravity = None
        self.particle_color = None
        self.particle_size = None
        self.is_sparkle = False
        
        self.particle_setup(x, y)
        
        if particle_color is not None:
            self.particle_color = particle_color
        
        if min_size is not None and max_size is not None:
            self.particle_size = random(min_size, max_size)
            

    def particle_setup(self, x, y):
        self.new_x = x
        self.old_x = self.new_x
        self.new_y = y
        self.old_y = self.new_y
      
        # Radiate particles 360 degree from center
        dir = random(0, TWO_PI)
      
        # Blast radius so the particle falls within the screen width
        firework_width = float(width) / (1.7 * width)
        magnitude = firework_width * random(10.1, 25)
        self.x_velocity = magnitude * cos(dir)
        self.y_velocity = magnitude * sin(dir)
      
        self.particle_size = random(1, 10)
        self.gravity = 0.2
        self.particle_color = '#FFFFFF'

    def draw(self):
        push()
      
        # Draw a line from the old location to the new location
        strokeWeight(int(self.particle_size))
        
        if self.is_sparkle:
            red_color = green_color = blue_color = None
            red_color   = red(self.particle_color) - random(50)
            green_color = green(self.particle_color) - random(50)
            blue_color  = blue(self.particle_color) - random(50)
            stroke(red_color, green_color, blue_color, random(255))
        else:
            stroke(self.particle_color)

        line(self.old_x, self.old_y, self.new_x, self.new_y)
      
        pop()


    def update(self):
        # Calculate new X and Y, set old X and Y
        self.old_x = self.new_x
        self.old_y = self.new_y
        self.new_x += self.x_velocity
        self.new_y += self.y_velocity
        self.y_velocity += self.gravity
        
        

add_library("minim")
global minim
minim = None
                
def play_sound(file_name):
    global minim
    if minim is not None:
        minim.stop()
    minim=Minim(this)
    s=minim.loadFile(file_name)
    s.play()

        
    
class FireworksDisplay:
    def __init__(self):
        self.fireworks = list()
        self.start_time_ms = None
        
    def add_firework(self, fw, launch_time_ms):
        self.fireworks.append( TimedFirework(fw, launch_time_ms) )

    def get_duration_ms(self):
        if self.start_time_ms is None:
            return 0
        
        return millis() - self.start_time_ms

    def launch(self):
        if self.start_time_ms is None:
            self.start_time_ms = millis()
            
        for fw in self.fireworks:
            if not fw.has_launched:
                if self.get_duration_ms() >= fw.launch_time_ms:
                    fw.firework.draw()
                    
                    if not fw.is_active():
                        self.fireworks[:] = [f for f in self.fireworks if f.is_active()]
                    
                    
class TimedFirework:    
    def __init__(self, fw, launch_time_ms):
      self.firework = fw
      self.launch_time_ms = launch_time_ms
      self.has_launched = False
    
    def is_active(self):
      return len(self.firework.particles) > 0
  

class Countdown:
    def __init__(self, starting_value_sec=10):
        self.start_val_sec = starting_value_sec
        self.font = loadFont("GillSans-UltraBold-100.vlw")
        self.start_time_ms = millis()

    def draw(self):
        textFont(self.font)
    
        elapsed_time_sec = ( millis() - self.start_time_ms ) / 1000
        if elapsed_time_sec > self.start_val_sec:
            text("Happy New Year!", width/2 - 550, height/2);
        else:
            text(int(self.start_val_sec - elapsed_time_sec), width/2 - 100, height/2);

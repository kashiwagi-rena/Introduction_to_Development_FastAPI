class Animal:
  height = 30

  def get_height(self):
    print(f"Animal {self.height}")

class Dog(Animal):
  height = 20

  def get_height(self):
    # 下記の書き方だと、Dogクラスのheightが出てくる
    print(f"Dog {self.height}")
    # 下記の書き方だと、Animalクラスのheightが出てくる
    # print(f"Parent {super.height}")

dog = Dog()
print(dog.get_height())
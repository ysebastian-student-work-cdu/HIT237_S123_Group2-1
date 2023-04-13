# Create your models here.
class Item_Class:
	
	def __init__(self, title = '', content = '', images = ''):
		self.title = title
		self.content = content
		self.images = images


	


reasons = Item_Class(
    title = 'Why food waste is a problem', 
    content = ['''
        <h2>
            Climate impact to a warming
        </h2>
        <p>
            What do flying, plastic production and oil extraction have in common? All these activities have a lower emissions impact on our warming planet than food waste.
            At an estimated 8% contributer of worldwide carbon emissions according to United Nations FAO, the everyday throwing away of that soggy lettuce you took too long to eat culminates into
            a much bigger impact on the planet than we thought.
        </p>
        <p>
            As it turns out, through minimal decision making each week, you can play your part in a significant role of helping to reduce worldwide carbon emissions by 8%. Sounds like a good deal to me!
        </p>''',
        '''
        <h2>
            Economic Impact
        </h2>
        <p>
            Food waste is quite costly, impacting the world economy $940 billion per year and the Australians economy around $36.6 billion each year according to the DCCEEW Government Department. But how does this affect the cost of
            your daily bread you ask? Consumers create the bulk of the cost too in through the third of a bag of groceries the avergae Australian wastes each week which has been estimated to cost you around $1438.55 (780 pounds) per year.
            Now that's expensive!
        </p>
        '''
        ],
    images = ['users/images/melting_globe.png', 'users/images/money_bin.jpg'])

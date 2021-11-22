class Test(object):
    def decorator(foo):
        def magic( self ) :
            print ("start magic")
            foo( self )
            print ("end magic")
        return magic

    @decorator
    def bar( self ) :
        print ("normal call")

test = Test()

test.bar()
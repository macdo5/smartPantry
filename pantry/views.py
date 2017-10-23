from django.shortcuts import render

# Create your views here.
@api_view(['POST'])
def get_full_pantry(request, pk):
    """
    Return the full pantry image, by calling the ImageSticher script
    """
    if request.method == 'POST':
        try:
            # get the pantry identified by the primary key
            pantry = Pantry.objects.get(pk=pk)
            # query the Java program to get the image path for the pantrys latest images

            # if successful, run the ImageStitching script to get the full pantry image
            
            # return the image made from the ImageStitching script.
            return HttpResponse(complete_img, content_type="image/png")
        except Pantry.DoesNotExist:
            
        
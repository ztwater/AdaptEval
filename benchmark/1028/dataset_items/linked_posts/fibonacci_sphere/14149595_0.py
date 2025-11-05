    private function moveTweets():void {


        var newScale:Number=Scale(meshes.length,50,500,6,2);
        trace("new scale:"+newScale);


        var l:Number=this.meshes.length;
        var tweetMeshInstance:TweetMesh;
        var destx:Number;
        var desty:Number;
        var destz:Number;
        for (var i:Number=0;i<this.meshes.length;i++){

            tweetMeshInstance=meshes[i];

            var phi:Number = Math.acos( -1 + ( 2 * i ) / l );
            var theta:Number = Math.sqrt( l * Math.PI ) * phi;

            tweetMeshInstance.origX = (sphereRadius+5) * Math.cos( theta ) * Math.sin( phi );
            tweetMeshInstance.origY= (sphereRadius+5) * Math.sin( theta ) * Math.sin( phi );
            tweetMeshInstance.origZ = (sphereRadius+5) * Math.cos( phi );

            destx=sphereRadius * Math.cos( theta ) * Math.sin( phi );
            desty=sphereRadius * Math.sin( theta ) * Math.sin( phi );
            destz=sphereRadius * Math.cos( phi );

            tweetMeshInstance.lookAt(new Vector3D());


            TweenMax.to(tweetMeshInstance, 1, {scaleX:newScale,scaleY:newScale,x:destx,y:desty,z:destz,onUpdate:onLookAtTween, onUpdateParams:[tweetMeshInstance]});

        }

    }
    private function onLookAtTween(theMesh:TweetMesh):void {
        theMesh.lookAt(new Vector3D());
    }

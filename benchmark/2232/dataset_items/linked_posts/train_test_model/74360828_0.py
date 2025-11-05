Vgg16 = keras.models.load_model(model1, compile=False)
Vgg16.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy' 
   , lr_track, keras.metrics.Precision(), keras.metrics.Recall()])

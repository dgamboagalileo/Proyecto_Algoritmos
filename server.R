
library(shiny)
library(reticulate)

source_python("algoritmos.py")

#tableOut, soluc = newtonSolverX(-5, "2x^5 - 3", 0.0001)

shinyServer(function(input, output) {
    
    #Evento y evaluación de metodo de newton para ceros
    newtonCalculate<-eventReactive(input$nwtSolver, {
        inputEcStr<-input$ecuacion[1]
        print(inputEcStr)
        initVal<-input$initVal[1]
        error<-input$Error[1]
        #outs<-add(initVal, error)
        outs<-newtonSolverX(initVal, inputEcStr, error)
        outs
    })
    
    #Evento y evaluación de diferencias finitas
    diferFinitCalculate<-eventReactive(input$diferFinEval, {
        inputEcStr<-input$difFinEcu[1]
        valX<-input$valorX[1]
        h<-input$valorH[1]
        outs<-evaluate_derivate_fx(inputEcStr, valX, h)
        as.character(outs)
    })
    
    #Evaluación diferencias finitas dos puntos
    finiteDifferenceTwoPoints<-eventReactive(input$difFinEvalTwoPoints, {
      inputEcStr<-input$difFinEcuTwoPoi[1]
      initVal<-input$valX[1]
      error<-input$valH[1]
      #outs<-add(initVal, error)
      outs<-finite_difference(inputEcStr, initVal, error)
      outs
    })
    
    #REnder metodo de Newton
    output$salidaTabla<-renderTable({
        newtonCalculate()
    })
    
    #Render Diferncias Finitas
    output$difFinitOut<-renderText({
        diferFinitCalculate()
    })
    
    #Render Diferncias Finitas dos puntos
    output$difFinOutTwoPoints<-renderTable({
      finiteDifferenceTwoPoints()
    })
    
})

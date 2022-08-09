library(shiny)
library(reticulate)
#C:/Users/Ferickcen/anaconda3

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
  
  #Evaluación diferencias finitas tres puntos
  finiteDifferenceThreePoints<-eventReactive(input$difFinEvalThreePoints, {
    inputEcStr<-input$difFinEcuThreePoi[1]
    initVal<-input$valX3[1]
    error<-input$valH3[1]
    #outs<-add(initVal, error)
    outs<-finite_difference3(inputEcStr, initVal, error)
    outs
  })
  
  #Evento y evaluación de Extrapolación Richardson
  richCalculate<-eventReactive(input$richEval, {
    inputEcStr<-input$richEcu[1]
    initVal<-input$valoX[1]
    error<-input$valoH[1]
    #outs<-add(initVal, error)
    outs<-extra_richards(inputEcStr, initVal, error)
    outs
  })
  
  #Evento y evaluación de Método de Trapezoides
  trapCalculate<-eventReactive(input$trapEval, {
    inputEcStr<-input$trapEcu[1]
    #initVal<-input$valoXtrap[1]
    a<-input$valoAtrap[1]
    b<-input$valoBtrap[1]
    n<-input$valoNtrap[1]
    #outs<-add(initVal, error)
    outs<-metodo_trapezoide(inputEcStr, a, b, n)
    outs
  })
  
  
  #Evento y evaluación de Extrapolación Richardson CDF
  richCalculateCDF<-eventReactive(input$richEvalCDF, {
    inputEcStr<-input$richEcuCDF[1]
    initVal<-input$valoXCDF[1]
    error<-input$valoHCDF[1]
    #outs<-add(initVal, error)
    outs<-extra_richardsCDF(inputEcStr, initVal, error)
    outs
  })
  
  
  #Evento y evaluación de Metodo Simpson
  simpsonCalculate<-eventReactive(input$simpsonEval, {
    inputEcStr<-input$simpEcu[1]
    a<-input$valASimpson[1]
    b<-input$valBSimpson[1]
    n<-input$valNSimpson[1]
    outs<-metodo_simpson(inputEcStr, a, b, n)
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
  
  #Render Metodo Trapezoides
  output$trapOut<-renderTable({
    trapCalculate()
  })
  
  #Render Diferncias Finitas dos puntos
  output$difFinOutTwoPoints<-renderTable({
    finiteDifferenceTwoPoints()
  })
  
  #Render Diferncias Finitas tres puntos
  output$difFinOutThreePoints<-renderTable({
    finiteDifferenceThreePoints()
  })
  
  #Render Extrapolacion Richardson
  output$richOut<-renderTable({
    richCalculate()
    
  })
  
  #Render Extrapolacion Richardson CDF
  output$richOutCDF<-renderTable({
    richCalculateCDF()
    
  })
  
  #Render metodo simpson
  output$simpsonOut<-renderTable({
    simpsonCalculate()
    
  })
})

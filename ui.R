library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
  dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Ceros", tabName = "Ceros"),
      menuItem("Derivación", tabName = "Derivacion"),
      menuItem("Diferencias Finitas", tabName = "DiferenciasfinitasDospuntos"),
      menuItem("Diferencias Finitas 3 Puntos", tabName = "DiferenciasfinitasTrespuntos"),
      menuItem("Richardson CDF", tabName = "ExtrapolacionRichardsonCDF"),
      menuItem("Richardson 3 Puntos", tabName = "ExtrapolacionRichardson"),
      menuItem("Metodo de Trapezoides", tabName = "MetodoTrapezoides"),
      menuItem("Metodo de Simpson", tabName = "MetodoSimpson")
      
    )
  ),
  dashboardBody(
    tabItems(
      tabItem("Ceros",
              h1("Método de Newton"),
              box(textInput("ecuacion", "Ingrese la Ecuación"),
                  textInput("initVal", "X0"),
                  textInput("Error", "Error")),
              actionButton("nwtSolver", "Newton Solver"),
              tableOutput("salidaTabla")),
      
      tabItem("Derivacion",
              h1("Diferencias Finitas"),
              box(textInput("difFinEcu", "Ingrese la Ecuación"),
                  textInput("valorX", "x"),
                  textInput("valorH", "h")),
              actionButton("diferFinEval", "Evaluar Derivada"),
              textOutput("difFinitOut")),
      
      tabItem("DiferenciasfinitasDospuntos",
              h1("Diferencias Finitas Dos Puntos"),
              box(textInput("difFinEcuTwoPoi", "Ingrese la Ecuación"),
                  textInput("valX", "x"),
                  textInput("valH", "h")),
              actionButton("difFinEvalTwoPoints", "Evaluar Derivada"),
              tableOutput("difFinOutTwoPoints")),
      
      tabItem("DiferenciasfinitasTrespuntos",
              h1("Diferencias Finitas Tres Puntos"),
              box(textInput("difFinEcuThreePoi", "Ingrese la Ecuación"),
                  textInput("valX3", "x"),
                  textInput("valH3", "h")),
              actionButton("difFinEvalThreePoints", "Evaluar"),
              tableOutput("difFinOutThreePoints")),
      
      tabItem("ExtrapolacionRichardson",
              h1("Extrapolación de Richardson con 3 Puntos"),
              box(textInput("richEcu", "Ingrese la Ecuación"),
                  textInput("valoX", "x"),
                  textInput("valoH", "h")),
              actionButton("richEval", "Evaluar"),
              tableOutput("richOut")),
      
      tabItem("ExtrapolacionRichardsonCDF",
              h1("Extrapolación de Richardson CDF"),
              box(textInput("richEcuCDF", "Ingrese la Ecuación"),
                  textInput("valoXCDF", "x"),
                  textInput("valoHCDF", "h")),
              actionButton("richEvalCDF", "Evaluar"),
              tableOutput("richOutCDF")),
      
      tabItem("MetodoTrapezoides",
              h1("Método de Trapezoides"),
              box(textInput("trapEcu", "Ingrese la Ecuación"),
                  #textInput("valoXtrap", "x"),
                  textInput("valoAtrap", "a"),
                  textInput("valoBtrap", "b"),
                  textInput("valoNtrap", "n")),
              actionButton("trapEval", "Evaluar"),
              tableOutput("trapOut")),
      
      tabItem("MetodoSimpson",
              h1("Método de Simpson"),
              box(textInput("simpEcu", "Ingrese la Ecuación"),
                  textInput("valASimpson", "a"),
                  textInput("valBSimpson", "b"),
                  textInput("valNSimpson", "n")),
              actionButton("simpsonEval", "Evaluar"),
              tableOutput("simpsonOut"))
      
    )
    
  )
  
)
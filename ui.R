library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Ceros", tabName = "Ceros"),
            menuItem("Derivación", tabName = "Derivacion"),
            menuItem("Diferencias Finitas Dos Puntos", tabName = "DiferenciasfinitasDospuntos")
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
                    tableOutput("difFinOutTwoPoints"))
        )
    )
)
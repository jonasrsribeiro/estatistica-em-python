from parte1.medidas_dispersao import calculo_dispersao
from parte1.medidas_estatisticas import calcula_estatisticas
import scipy.stats as stats

umidadeBahiaBelmonte = [90.0,94.0,94.0,94.0,94.0,93.0,77.0,70.0,62.0,60.0,58.0,50.0,46.0,44.0,59.0,66.0,72.0,79.0,93.0,89.0,82.0,64.0,61.0,60.0,60.0,67.0,69.0,69.0,71.0,77.0,81.0,83.0,89.0,90.0,92.0,93.0,93.0,93.0,94.0,94.0,95.0,95.0,91.0,81.0,77.0,71.0,67.0,61.0,69.0,69.0,65.0,74.0,78.0,82.0,87.0,89.0,91.0,92.0,93.0,93.0,93.0,94.0,94.0,94.0,94.0,95.0,93.0,83.0,77.0,68.0,67.0,69.0,58.0,66.0,65.0,89.0,89.0,91.0,92.0,93.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,81.0,77.0,68.0,64.0,58.0,61.0,60.0,65.0,61.0,64.0,75.0,80.0,93.0,94.0,94.0,94.0,94.0,95.0,93.0,78.0,67.0,62.0,52.0,52.0,46.0,48.0,46.0,49.0,57.0,68.0,81.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,81.0,73.0,72.0,91.0,88.0,74.0,72.0,76.0,73.0,76.0,83.0,88.0,93.0,93.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,79.0,70.0,59.0,53.0,51.0,51.0,56.0,55.0,58.0,64.0,77.0,86.0,91.0,91.0,92.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,94.0,92.0,81.0,72.0,72.0,71.0,67.0,57.0,60.0,62.0,66.0,77.0,85.0,90.0,93.0,94.0,95.0,94.0,95.0,95.0,95.0,80.0,75.0,68.0,62.0,55.0,52.0,53.0,55.0,59.0,66.0,76.0,81.0,94.0,93.0,78.0,70.0,67.0,55.0,50.0,51.0,46.0,47.0,65.0,67.0,71.0,79.0,89.0,91.0,89.0,93.0,93.0,93.0,94.0,94.0,93.0,92.0,89.0,87.0,89.0,87.0,89.0,86.0,86.0,87.0,90.0,91.0,93.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,94.0,82.0,72.0,63.0,56.0,68.0,79.0,67.0,65.0,75.0,72.0,82.0,87.0,90.0,92.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,85.0,72.0,67.0,65.0,59.0,62.0,58.0,58.0,63.0,76.0,86.0,90.0,91.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,93.0,74.0,68.0,60.0,55.0,67.0,59.0,67.0,66.0,62.0,72.0,80.0,84.0,93.0,94.0,94.0,94.0,94.0,95.0,95.0,94.0,76.0,72.0,60.0,56.0,65.0,56.0,64.0,68.0,59.0,67.0,74.0,80.0,93.0,94.0,94.0,94.0,94.0,94.0,95.0,91.0,75.0,70.0,64.0,56.0,53.0,53.0,54.0,58.0,62.0,70.0,75.0,79.0,93.0,94.0,94.0,94.0,95.0,95.0,77.0,73.0,65.0,52.0,49.0,49.0,47.0,41.0,51.0,66.0,75.0,81.0,93.0,93.0,94.0,94.0,94.0,94.0,95.0,93.0,76.0,68.0,56.0,57.0,45.0,51.0,50.0,61.0,55.0,61.0,79.0,87.0,93.0,94.0,94.0,94.0,94.0,95.0,94.0,75.0,66.0,55.0,54.0,49.0,50.0,45.0,49.0,54.0,62.0,75.0,79.0,93.0,94.0,94.0,94.0,94.0,95.0,86.0,84.0,65.0,55.0,53.0,55.0,54.0,60.0,57.0,60.0,71.0,81.0,92.0,94.0,94.0,85.0,75.0,69.0,57.0,55.0,53.0,49.0,47.0,51.0,50.0,57.0,67.0,77.0,94.0,94.0,94.0,89.0,73.0,82.0,65.0,61.0,59.0,55.0,47.0,52.0,49.0,67.0,76.0,87.0,91.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,94.0,75.0,69.0,62.0,60.0,53.0,52.0,50.0,51.0,60.0,68.0,79.0,86.0,91.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,84.0,81.0,73.0,77.0,72.0,64.0,73.0,63.0,73.0,76.0,83.0,87.0,90.0,92.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,81.0,73.0,71.0,65.0,61.0,60.0,63.0,71.0,77.0,86.0,91.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,94.0,80.0,72.0,66.0,69.0,61.0,71.0,63.0,65.0,66.0,74.0,83.0,88.0,92.0,93.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,94.0,85.0,71.0,67.0,66.0,82.0,85.0,90.0,90.0,91.0,92.0,92.0,91.0,91.0,92.0,92.0,93.0,93.0,93.0,93.0,94.0,94.0,94.0,93.0,83.0,77.0,69.0,62.0,66.0,62.0,60.0,57.0,66.0,70.0,83.0,88.0,92.0,93.0,93.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,94.0,83.0,76.0,77.0,59.0,63.0,56.0,56.0,54.0,66.0,68.0,78.0,85.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,94.0,75.0,67.0,64.0,54.0,52.0,51.0,47.0,57.0,60.0,67.0,76.0,82.0,91.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,90.0,80.0,72.0,71.0,68.0,75.0,76.0,76.0,85.0,87.0,90.0,91.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,90.0,77.0,73.0,71.0,69.0,71.0,64.0,74.0,81.0,76.0,81.0,87.0,90.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,87.0,73.0,66.0,61.0,66.0,63.0,65.0,84.0,81.0,80.0,86.0,90.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,92.0,83.0,74.0,68.0,63.0,72.0,63.0,93.0,94.0,94.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,93.0,89.0,84.0,77.0,72.0,67.0,60.0,58.0,54.0,59.0,69.0,80.0,88.0,91.0,93.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,94.0,87.0,83.0,71.0,81.0,79.0,81.0,67.0,64.0,72.0,73.0,85.0,87.0,92.0,94.0,94.0,94.0,94.0,93.0,92.0,92.0,93.0,94.0,85.0,76.0,68.0,60.0,56.0,53.0,53.0,53.0,54.0,58.0,66.0,80.0,89.0,92.0,93.0,94.0,94.0,94.0,93.0,94.0,94.0,94.0,94.0,94.0,90.0,79.0,72.0,68.0,60.0,58.0,55.0,67.0,76.0,86.0,90.0,92.0,93.0,93.0,93.0,94.0,93.0,94.0,93.0,94.0,94.0,94.0,94.0,94.0,87.0,74.0,68.0,63.0,64.0,65.0,67.0,69.0,73.0,79.0,86.0,90.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,93.0,81.0,73.0,66.0,61.0,60.0,74.0,82.0,85.0,79.0,84.0,90.0,93.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,85.0,77.0,62.0,60.0,64.0,59.0,60.0,61.0,63.0,71.0,82.0,90.0,92.0,93.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,94.0,81.0,75.0,68.0,71.0,70.0,63.0,61.0,60.0,68.0,73.0,83.0,87.0,90.0,92.0,93.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,92.0,81.0,75.0,68.0,89.0,73.0,77.0,71.0,73.0,74.0,81.0,84.0,88.0,87.0,89.0,91.0,92.0,93.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,93.0,93.0,94.0,93.0,92.0,92.0,88.0,84.0,83.0,85.0,91.0,93.0,93.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,93.0,89.0,84.0,88.0,90.0,86.0,93.0,89.0,92.0,93.0,94.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,90.0,91.0,84.0,76.0,87.0,86.0,91.0,88.0,86.0,91.0,92.0,92.0,93.0,93.0,93.0,92.0,93.0,94.0,94.0,94.0,94.0,95.0,94.0,94.0,83.0,75.0,66.0,67.0,61.0,56.0,54.0,53.0,60.0,71.0,89.0,92.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,87.0,75.0,70.0,65.0,81.0,82.0,60.0,64.0,71.0,75.0,88.0,92.0,93.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,80.0,77.0,77.0,72.0,89.0,82.0,79.0,90.0,91.0,92.0,91.0,90.0,90.0,90.0,93.0,93.0,93.0,93.0,93.0,93.0,93.0,93.0,94.0,92.0,89.0,84.0,86.0,88.0,86.0,78.0,67.0,63.0,69.0,72.0,74.0,73.0,80.0,91.0,92.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,91.0,89.0,84.0,80.0,79.0,88.0,90.0,88.0,92.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,88.0,86.0,81.0,82.0,77.0,76.0,68.0,64.0,86.0,91.0,92.0,93.0,93.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,85.0,78.0,72.0,67.0,62.0,58.0,61.0,61.0,66.0,76.0,85.0,91.0,93.0,94.0,94.0,95.0,94.0,95.0,95.0,95.0,95.0,95.0,86.0,81.0,78.0,66.0,61.0,66.0,69.0,71.0,72.0,82.0,90.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,95.0,89.0,74.0,64.0,54.0,54.0,54.0,58.0,56.0,61.0,71.0,83.0,89.0,91.0,92.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,93.0,93.0,92.0,89.0,85.0,78.0,80.0,72.0,70.0,72.0,71.0,75.0,86.0,86.0,92.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,92.0,87.0,82.0,89.0,91.0,92.0,91.0,89.0,88.0,87.0,88.0,89.0,92.0,92.0,89.0,89.0,90.0,90.0,90.0,93.0,93.0,94.0,94.0,94.0,92.0,89.0,85.0,83.0,83.0,90.0,88.0,81.0,81.0,82.0,89.0,92.0,93.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,91.0,77.0,67.0,62.0,56.0,62.0,65.0,65.0,70.0,78.0,88.0,92.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,95.0,95.0,93.0,79.0,68.0,70.0,84.0,85.0,73.0,81.0,81.0,84.0,90.0,93.0,93.0,93.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,92.0,81.0,76.0,65.0,66.0,64.0,67.0,68.0,77.0,88.0,92.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,95.0,96.0,96.0,87.0,73.0,62.0,68.0,68.0,64.0,63.0,59.0,63.0,74.0,88.0,93.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,95.0,95.0,95.0,95.0,95.0,85.0,74.0,72.0,65.0,63.0,74.0,84.0,80.0,85.0,89.0,89.0,91.0,92.0,93.0,93.0,94.0,94.0,95.0,95.0,95.0,96.0,95.0,80.0,71.0,62.0,57.0,58.0,54.0,61.0,61.0,65.0,75.0,84.0,89.0,93.0,93.0,93.0,93.0,93.0,94.0,94.0,95.0,94.0,95.0,95.0,94.0,91.0,89.0,93.0,91.0,82.0,75.0,71.0,68.0,71.0,78.0,89.0,90.0,91.0,92.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,86.0,73.0,67.0,67.0,64.0,61.0,62.0,63.0,78.0,81.0,89.0,92.0,93.0,94.0,94.0,95.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,92.0,85.0,85.0,69.0,65.0,65.0,62.0,65.0,69.0,76.0,87.0,91.0,93.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,88.0,79.0,75.0,69.0,67.0,62.0,63.0,64.0,69.0,77.0,88.0,93.0,94.0,94.0,95.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,90.0,80.0,74.0,73.0,62.0,66.0,68.0,67.0,75.0,81.0,88.0,91.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,94.0,94.0,92.0,90.0,91.0,89.0,89.0,89.0,89.0,90.0,90.0,91.0,93.0,94.0,94.0,94.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,93.0,85.0,78.0,63.0,69.0,65.0,66.0,68.0,77.0,83.0,91.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,85.0,74.0,70.0,69.0,56.0,61.0,65.0,68.0,71.0,79.0,86.0,91.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,86.0,76.0,70.0,63.0,60.0,55.0,56.0,52.0,68.0,76.0,86.0,89.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,91.0,77.0,74.0,59.0,51.0,51.0,45.0,49.0,54.0,78.0,89.0,92.0,93.0,93.0,95.0,95.0,95.0,96.0,96.0,96.0,94.0,80.0,74.0,62.0,59.0,63.0,57.0,61.0,64.0,76.0,89.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,95.0,89.0,70.0,61.0,53.0,59.0,57.0,62.0,65.0,74.0,86.0,92.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,91.0,78.0,76.0,64.0,60.0,58.0,59.0,60.0,63.0,72.0,89.0,92.0,94.0,94.0,95.0,95.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,91.0,88.0,83.0,67.0,61.0,61.0,63.0,66.0,65.0,75.0,89.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,96.0,96.0,96.0,90.0,75.0,65.0,60.0,54.0,51.0,51.0,47.0,66.0,75.0,85.0,91.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,93.0,75.0,69.0,66.0,72.0,77.0,73.0,78.0,81.0,87.0,88.0,87.0,91.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,81.0,76.0,67.0,60.0,63.0,62.0,61.0,61.0,68.0,75.0,86.0,91.0,93.0,94.0,94.0,93.0,94.0,94.0,94.0,95.0,93.0,94.0,94.0,94.0,84.0,75.0,65.0,57.0,52.0,54.0,53.0,69.0,73.0,79.0,82.0,85.0,86.0,84.0,88.0,91.0,93.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,89.0,81.0,71.0,53.0,47.0,47.0,45.0,48.0,57.0,70.0,87.0,92.0,92.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,73.0,64.0,52.0,46.0,47.0,48.0,59.0,62.0,70.0,84.0,90.0,93.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,96.0,96.0,85.0,71.0,64.0,61.0,56.0,55.0,55.0,64.0,69.0,72.0,87.0,91.0,93.0,93.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,88.0,73.0,63.0,60.0,55.0,43.0,52.0,53.0,61.0,72.0,81.0,84.0,89.0,90.0,92.0,94.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,93.0,80.0,75.0,90.0,79.0,72.0,87.0,84.0,87.0,91.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,96.0,96.0,96.0,86.0,77.0,72.0,75.0,64.0,66.0,60.0,66.0,63.0,74.0,90.0,93.0,94.0,94.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,96.0,96.0,96.0,93.0,78.0,70.0,64.0,58.0,57.0,65.0,69.0,75.0,80.0,88.0,92.0,93.0,95.0,95.0,95.0,95.0,95.0,96.0,96.0,96.0,96.0,96.0,93.0,79.0,76.0,61.0,63.0,66.0,65.0,61.0,67.0,77.0,86.0,91.0,93.0,92.0,90.0,92.0,93.0,94.0,94.0,94.0,94.0,93.0,93.0,94.0,94.0,93.0,93.0,91.0,91.0,92.0,90.0,92.0,93.0,93.0,93.0,94.0,94.0]

umidadeSaoPauloTaubate = [75.0,82.0,86.0,84.0,89.0,91.0,92.0,92.0,93.0,93.0,92.0,88.0,75.0,67.0,62.0,60.0,54.0,58.0,58.0,74.0,74.0,76.0,79.0,74.0,79.0,72.0,72.0,70.0,73.0,78.0,82.0,83.0,87.0,89.0,79.0,78.0,74.0,64.0,60.0,58.0,57.0,49.0,49.0,49.0,57.0,65.0,71.0,77.0,78.0,79.0,77.0,83.0,86.0,90.0,91.0,92.0,92.0,92.0,89.0,82.0,72.0,59.0,57.0,58.0,52.0,48.0,46.0,45.0,44.0,47.0,43.0,47.0,61.0,67.0,75.0,79.0,88.0,80.0,82.0,87.0,88.0,88.0,81.0,76.0,69.0,57.0,42.0,41.0,38.0,41.0,43.0,41.0,36.0,49.0,51.0,56.0,64.0,70.0,78.0,83.0,88.0,90.0,91.0,91.0,92.0,92.0,88.0,80.0,73.0,64.0,51.0,46.0,45.0,42.0,50.0,75.0,69.0,71.0,73.0,77.0,78.0,81.0,86.0,86.0,88.0,90.0,89.0,92.0,93.0,93.0,93.0,86.0,79.0,76.0,66.0,59.0,55.0,54.0,50.0,62.0,66.0,71.0,76.0,85.0,84.0,83.0,84.0,86.0,93.0,93.0,92.0,93.0,93.0,92.0,92.0,88.0,79.0,70.0,64.0,59.0,56.0,68.0,69.0,61.0,67.0,72.0,76.0,77.0,81.0,82.0,89.0,88.0,91.0,91.0,90.0,90.0,91.0,91.0,87.0,82.0,77.0,74.0,66.0,62.0,58.0,50.0,53.0,62.0,71.0,81.0,85.0,86.0,84.0,85.0,85.0,86.0,89.0,90.0,91.0,92.0,92.0,92.0,92.0,89.0,75.0,70.0,61.0,56.0,52.0,63.0,82.0,84.0,93.0,86.0,90.0,91.0,92.0,90.0,90.0,92.0,93.0,93.0,94.0,93.0,94.0,93.0,93.0,83.0,77.0,73.0,67.0,62.0,55.0,64.0,54.0,60.0,57.0,65.0,72.0,77.0,79.0,85.0,87.0,91.0,85.0,88.0,88.0,89.0,91.0,91.0,90.0,86.0,66.0,70.0,62.0,53.0,55.0,54.0,53.0,57.0,65.0,72.0,77.0,74.0,76.0,77.0,76.0,78.0,75.0,77.0,81.0,79.0,81.0,82.0,86.0,85.0,79.0,76.0,71.0,70.0,67.0,68.0,69.0,67.0,70.0,74.0,77.0,82.0,82.0,82.0,83.0,84.0,85.0,87.0,89.0,88.0,87.0,87.0,85.0,84.0,77.0,72.0,67.0,63.0,60.0,54.0,47.0,48.0,62.0,70.0,75.0,78.0,80.0,83.0,88.0,89.0,90.0,91.0,90.0,91.0,91.0,91.0,91.0,88.0,81.0,74.0,65.0,55.0,50.0,45.0,46.0,48.0,41.0,53.0,61.0,67.0,68.0,76.0,83.0,86.0,86.0,87.0,91.0,91.0,93.0,93.0,92.0,85.0,74.0,59.0,52.0,47.0,39.0,37.0,32.0,33.0,44.0,52.0,65.0,73.0,71.0,78.0,80.0,84.0,87.0,89.0,89.0,91.0,92.0,92.0,91.0,77.0,68.0,58.0,50.0,40.0,38.0,38.0,36.0,33.0,46.0,56.0,68.0,72.0,73.0,78.0,82.0,84.0,86.0,88.0,91.0,91.0,91.0,92.0,86.0,75.0,69.0,62.0,52.0,47.0,47.0,44.0,54.0,54.0,59.0,68.0,67.0,73.0,94.0,93.0,93.0,93.0,94.0,93.0,94.0,94.0,94.0,94.0,94.0,89.0,76.0,71.0,66.0,60.0,55.0,55.0,57.0,65.0,68.0,72.0,77.0,84.0,87.0,86.0,91.0,92.0,93.0,94.0,94.0,94.0,95.0,94.0,93.0,92.0,88.0,80.0,75.0,67.0,61.0,54.0,49.0,58.0,60.0,71.0,74.0,75.0,79.0,80.0,80.0,87.0,92.0,93.0,93.0,92.0,92.0,93.0,92.0,90.0,83.0,77.0,64.0,62.0,58.0,57.0,58.0,70.0,80.0,73.0,84.0,87.0,90.0,90.0,92.0,92.0,93.0,94.0,93.0,94.0,94.0,94.0,93.0,85.0,69.0,63.0,59.0,49.0,48.0,49.0,51.0,49.0,51.0,52.0,76.0,79.0,85.0,85.0,74.0,78.0,94.0,95.0,95.0,94.0,93.0,92.0,92.0,91.0,91.0,90.0,91.0,92.0,83.0,79.0,76.0,73.0,77.0,77.0,87.0,88.0,87.0,89.0,90.0,91.0,94.0,94.0,94.0,92.0,91.0,89.0,88.0,87.0,86.0,77.0,72.0,70.0,63.0,76.0,91.0,90.0,91.0,93.0,93.0,91.0,91.0,92.0,93.0,92.0,93.0,93.0,92.0,93.0,93.0,93.0,93.0,92.0,91.0,89.0,88.0,90.0,89.0,90.0,87.0,85.0,88.0,91.0,91.0,91.0,92.0,93.0,94.0,94.0,95.0,95.0,94.0,95.0,95.0,95.0,94.0,91.0,82.0,76.0,70.0,70.0,63.0,61.0,63.0,58.0,65.0,69.0,72.0,85.0,85.0,89.0,92.0,91.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,88.0,83.0,85.0,80.0,77.0,72.0,70.0,74.0,77.0,64.0,73.0,75.0,78.0,79.0,90.0,91.0,92.0,93.0,92.0,93.0,93.0,93.0,94.0,94.0,93.0,90.0,92.0,89.0,82.0,83.0,84.0,87.0,90.0,92.0,92.0,92.0,91.0,92.0,92.0,92.0,92.0,93.0,92.0,93.0,93.0,93.0,93.0,93.0,93.0,93.0,92.0,90.0,87.0,88.0,87.0,85.0,84.0,86.0,92.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,93.0,88.0,82.0,78.0,74.0,67.0,66.0,65.0,69.0,81.0,90.0,92.0,94.0,94.0,95.0,94.0,94.0,94.0,94.0,94.0,94.0,94.0,93.0,93.0,93.0,87.0,80.0,76.0,76.0,67.0,63.0,59.0,53.0,54.0,64.0,70.0,75.0,77.0,83.0,88.0,91.0,93.0,93.0,94.0,94.0,94.0,95.0,95.0,95.0,91.0,85.0,77.0,69.0,60.0,45.0,38.0,39.0,37.0,39.0,51.0,63.0,63.0,67.0,75.0,85.0,87.0,90.0,91.0,88.0,88.0,86.0,87.0,84.0,84.0,77.0,70.0,61.0,58.0,46.0,40.0,37.0,38.0,41.0,68.0,76.0,79.0,79.0,81.0,83.0,86.0,91.0,89.0,90.0,89.0,90.0,91.0,90.0,87.0,82.0,76.0,70.0,66.0,56.0,48.0,55.0,57.0,66.0,69.0,74.0,86.0,89.0,90.0,92.0,93.0,91.0,93.0,93.0,93.0,94.0,94.0,93.0,88.0,76.0,67.0,54.0,49.0,46.0,41.0,41.0,43.0,45.0,62.0,70.0,74.0,74.0,78.0,82.0,85.0,92.0,92.0,92.0,92.0,92.0,94.0,92.0,88.0,84.0,74.0,65.0,60.0,52.0,51.0,47.0,45.0,51.0,62.0,69.0,72.0,76.0,79.0,81.0,81.0,82.0,88.0,92.0,93.0,92.0,93.0,93.0,84.0,78.0,69.0,64.0,57.0,45.0,42.0,40.0,39.0,45.0,55.0,62.0,64.0,74.0,76.0,82.0,87.0,88.0,89.0,85.0,89.0,90.0,88.0,89.0,83.0,71.0,65.0,60.0,56.0,50.0,53.0,51.0,53.0,56.0,60.0,67.0,72.0,76.0,79.0,82.0,84.0,87.0,89.0,87.0,91.0,91.0,92.0,94.0,83.0,71.0,63.0,59.0,57.0,53.0,49.0,51.0,48.0,68.0,75.0,78.0,80.0,82.0,84.0,88.0,90.0,92.0,93.0,93.0,93.0,93.0,93.0,92.0,88.0,80.0,73.0,68.0,59.0,47.0,52.0,57.0,52.0,59.0,68.0,83.0,86.0,79.0,90.0,89.0,90.0,89.0,91.0,91.0,91.0,93.0,93.0,93.0,86.0,81.0,72.0,62.0,57.0,56.0,53.0,53.0,53.0,63.0,79.0,80.0,78.0,80.0,85.0,88.0,91.0,92.0,93.0,94.0,94.0,94.0,94.0,93.0,89.0,90.0,83.0,72.0,64.0,57.0,52.0,45.0,55.0,59.0,68.0,76.0,75.0,74.0,79.0,89.0,91.0,92.0,92.0,93.0,93.0,94.0,93.0,92.0,82.0,74.0,74.0,68.0,62.0,60.0,49.0,60.0,76.0,72.0,74.0,75.0,77.0,78.0,79.0,87.0,89.0,94.0,94.0,93.0,93.0,93.0,93.0,90.0,85.0,79.0,71.0,63.0,59.0,57.0,54.0,54.0,54.0,68.0,73.0,75.0,76.0,75.0,76.0,78.0,78.0,83.0,85.0,88.0,88.0,91.0,91.0,91.0,81.0,72.0,67.0,65.0,60.0,54.0,53.0,56.0,56.0,62.0,71.0,75.0,79.0,80.0,84.0,83.0,89.0,88.0,91.0,92.0,92.0,91.0,91.0,89.0,85.0,79.0,70.0,68.0,62.0,53.0,56.0,59.0,63.0,67.0,72.0,79.0,82.0,84.0,83.0,84.0,85.0,87.0,83.0,84.0,85.0,86.0,86.0,86.0,81.0,77.0,69.0,62.0,55.0,53.0,51.0,51.0,54.0,61.0,66.0,69.0,72.0,77.0,81.0,83.0,84.0,83.0,86.0,86.0,86.0,88.0,87.0,82.0,73.0,69.0,65.0,56.0,53.0,48.0,48.0,47.0,48.0,53.0,67.0,69.0,75.0,77.0,87.0,88.0,90.0,90.0,88.0,88.0,88.0,89.0,90.0,87.0,86.0,80.0,76.0,68.0,64.0,56.0,51.0,52.0,52.0,73.0,77.0,88.0,88.0,88.0,89.0,91.0,91.0,92.0,90.0,87.0,85.0,89.0,88.0,92.0,90.0,89.0,81.0,72.0,69.0,69.0,69.0,74.0,74.0,73.0,75.0,76.0,75.0,76.0,76.0,77.0,80.0,82.0,82.0,83.0,88.0,91.0,88.0,89.0,84.0,75.0,73.0,67.0,68.0,65.0,67.0,68.0,69.0,69.0,74.0,71.0,76.0,91.0,93.0,92.0,90.0,91.0,90.0,88.0,89.0,92.0,94.0,95.0,83.0,73.0,69.0,65.0,62.0,58.0,55.0,55.0,54.0,60.0,72.0,78.0,85.0,86.0,85.0,85.0,91.0,91.0,90.0,91.0,92.0,91.0,91.0,91.0,86.0,85.0,77.0,69.0,64.0,63.0,59.0,55.0,56.0,58.0,71.0,82.0,87.0,89.0,91.0,91.0,92.0,93.0,92.0,93.0,93.0,93.0,94.0,93.0,83.0,74.0,65.0,52.0,36.0,29.0,30.0,30.0,32.0,37.0,67.0,71.0,78.0,82.0,85.0,87.0,89.0,90.0,90.0,90.0,92.0,90.0,93.0,93.0,81.0,73.0,62.0,53.0,45.0,35.0,33.0,33.0,29.0,39.0,61.0,74.0,83.0,87.0,86.0,91.0,89.0,91.0,89.0,91.0,91.0,91.0,93.0,89.0,80.0,64.0,56.0,52.0,45.0,38.0,33.0,32.0,33.0,45.0,62.0,77.0,75.0,71.0,71.0,78.0,81.0,81.0,83.0,89.0,89.0,92.0,90.0,92.0,83.0,71.0,64.0,60.0,55.0,53.0,49.0,49.0,64.0,68.0,74.0,77.0,79.0,80.0,83.0,85.0,84.0,83.0,83.0,84.0,87.0,90.0,92.0,92.0,80.0,81.0,77.0,69.0,65.0,60.0,57.0,56.0,59.0,64.0,73.0,80.0,82.0,84.0,85.0,88.0,90.0,91.0,88.0,90.0,90.0,90.0,89.0,91.0,87.0,76.0,69.0,61.0,56.0,50.0,46.0,45.0,46.0,50.0,64.0,75.0,86.0,88.0,91.0,92.0,92.0,93.0,93.0,93.0,93.0,93.0,93.0,92.0,83.0,78.0,63.0,52.0,43.0,42.0,40.0,46.0,48.0,58.0,66.0,82.0,85.0,88.0,87.0,87.0,88.0,91.0,90.0,92.0,93.0,94.0,95.0,95.0,85.0,72.0,66.0,60.0,53.0,50.0,47.0,44.0,46.0,55.0,61.0,70.0,82.0,86.0,88.0,90.0,90.0,91.0,93.0,93.0,94.0,93.0,94.0,93.0,83.0,71.0,61.0,50.0,39.0,34.0,32.0,33.0,33.0,50.0,62.0,75.0,83.0,85.0,87.0,88.0,89.0,87.0,90.0,90.0,92.0,93.0,92.0,91.0,80.0,75.0,67.0,53.0,45.0,33.0,32.0,38.0,42.0,50.0,71.0,77.0,81.0,83.0,86.0,87.0,89.0,91.0,93.0,91.0,91.0,92.0,93.0,92.0,83.0,70.0,56.0,48.0,39.0,37.0,39.0,39.0,35.0,37.0,57.0,74.0,76.0,83.0,86.0,89.0,88.0,87.0,91.0,91.0,91.0,91.0,92.0,92.0,82.0,69.0,56.0,55.0,44.0,35.0,32.0,34.0,34.0,44.0,63.0,73.0,81.0,82.0,81.0,80.0,88.0,90.0,91.0,92.0,91.0,92.0,93.0,92.0,86.0,79.0,66.0,56.0,47.0,43.0,34.0,32.0,35.0,44.0,65.0,79.0,82.0,85.0,85.0,90.0,90.0,92.0,92.0,92.0,92.0,91.0,92.0,89.0,81.0,67.0,63.0,55.0,50.0,41.0,32.0,28.0,28.0,45.0,62.0,76.0,82.0,81.0,85.0,85.0,90.0,90.0,91.0,92.0,91.0,92.0,92.0,91.0,79.0,73.0,63.0,52.0,45.0,41.0,37.0,31.0,34.0,44.0,64.0,76.0,85.0,84.0,88.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,50.0,44.0,40.0,41.0,45.0,53.0,64.0,76.0,83.0,88.0,90.0,92.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,39.0,39.0,41.0,47.0,71.0,80.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,55.0,51.0,45.0,39.0,40.0,37.0,36.0,44.0,72.0,64.0,73.0,77.0,83.0,90.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,71.0,63.0,56.0,51.0,42.0,40.0,40.0,50.0,72.0,79.0,85.0,87.0,87.0,91.0,91.0,90.0,90.0,91.0,92.0,92.0,94.0,94.0,94.0,95.0,83.0,70.0,56.0,47.0,41.0,41.0,46.0,50.0,62.0,78.0,84.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,82.0,72.0,63.0,47.0,37.0,34.0,32.0,35.0,33.0,42.0,69.0,73.0,77.0,85.0,86.0,88.0,89.0,91.0,92.0,92.0,93.0,90.0,91.0,92.0,79.0,67.0,43.0,33.0,33.0,31.0,30.0,28.0,28.0,31.0,41.0,65.0,79.0,82.0,81.0,83.0,84.0,87.0,87.0,0.0,0.0,0.0,0.0,0.0,0.0,76.0,71.0,65.0,55.0,55.0,61.0,70.0,79.0,79.0,84.0,88.0,90.0,91.0,91.0,89.0,90.0,89.0,88.0,86.0,0.0,0.0,0.0,0.0,0.0,81.0,76.0,73.0,74.0,71.0,70.0,70.0,76.0,78.0,79.0,80.0,83.0,82.0,85.0,90.0,92.0,92.0,91.0,90.0,0.0,0.0,0.0,0.0,0.0,79.0,76.0,73.0,68.0,61.0,55.0,49.0,48.0,52.0,76.0,81.0,86.0,88.0,91.0,91.0,92.0,92.0,93.0,92.0,92.0,92.0,94.0,92.0,85.0,71.0,61.0,49.0,41.0,36.0,32.0,32.0,33.0,36.0,61.0,70.0,77.0,80.0,84.0,88.0,86.0,87.0,87.0,90.0,90.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,57.0,54.0,54.0,51.0,52.0,59.0,69.0,76.0,76.0,78.0,81.0,84.0,90.0,91.0,92.0,92.0,91.0,89.0,86.0,89.0,84.0,79.0,74.0,64.0,60.0,54.0,49.0,46.0,49.0,65.0,75.0,80.0,79.0,80.0,81.0,81.0,82.0,82.0,84.0,84.0,86.0,88.0,89.0,89.0,87.0,85.0,80.0,71.0,66.0,62.0,60.0,58.0,60.0,65.0,73.0,77.0,84.0,85.0,90.0,91.0,87.0,88.0,88.0,87.0,87.0,89.0,88.0,91.0,88.0,81.0,74.0,70.0,63.0,55.0,52.0,47.0,48.0,49.0,73.0,82.0,87.0,88.0,90.0,90.0,91.0,92.0,93.0,94.0,93.0,94.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,54.0,44.0,35.0,37.0,33.0,38.0,82.0,83.0,83.0,88.0,89.0,93.0,93.0,94.0,94.0,94.0,94.0,92.0,91.0,93.0,92.0,92.0,87.0,84.0,71.0,68.0,61.0,62.0,61.0,68.0,72.0,74.0,77.0,78.0,78.0,81.0,88.0,85.0,83.0,84.0,82.0,91.0,92.0,93.0,94.0,91.0,89.0,92.0,94.0,92.0,88.0,90.0,88.0,88.0,88.0,89.0,92.0,94.0,94.0,95.0,95.0,95.0,92.0,92.0,92.0,92.0,92.0,94.0,94.0,95.0,95.0,94.0,94.0,94.0,92.0,91.0,90.0,89.0,89.0,90.0,93.0,93.0,94.0,93.0,93.0,92.0,92.0,92.0,93.0,94.0,94.0,94.0,94.0,93.0,92.0,90.0,89.0,83.0,76.0,71.0,62.0,61.0,55.0,47.0,54.0,72.0,84.0,84.0,89.0,86.0,92.0,84.0,81.0,79.0,77.0,79.0,0.0,0.0,0.0,0.0,0.0,0.0,60.0,52.0,48.0,43.0,29.0,44.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,59.0,54.0,52.0,50.0,48.0,50.0,51.0,54.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,78.0,63.0,55.0,52.0,49.0,47.0,47.0,57.0,71.0,76.0,78.0]

somaBahiaBelmonte = sum(umidadeBahiaBelmonte)
somaSaoPauloTaubate = sum(umidadeSaoPauloTaubate)

mediaBahiaBelmonte, a, b = calcula_estatisticas(umidadeBahiaBelmonte)
mediaSaoPauloTaubate, a, b = calcula_estatisticas(umidadeSaoPauloTaubate)

termoA = (((somaBahiaBelmonte ** 2) / 2) + ((somaSaoPauloTaubate ** 2) / 2))
termoB = ((somaBahiaBelmonte + somaSaoPauloTaubate) ** 2) / 4

somaDosQuadradosEntreGrupos = termoA - termoB

somaDosQuadradosDentroDosGrupos = sum((umidadeBahiaBelmonte[i] - mediaBahiaBelmonte) ** 2 + (umidadeSaoPauloTaubate[i] - mediaSaoPauloTaubate) ** 2 for i in range(len(umidadeBahiaBelmonte)))

print('Soma dos quadrados entre grupos:', round(somaDosQuadradosEntreGrupos,2))
print('Soma dos quadrados dentro dos grupos:', round(somaDosQuadradosDentroDosGrupos,2))

grausDeLiberdadeEntreGrupos = 2 - 1
grausDeLiberdadeDentroDosGrupos = (somaBahiaBelmonte + somaSaoPauloTaubate) - 2

print('Graus de liberdade entre grupos:', grausDeLiberdadeEntreGrupos)
print('Graus de liberdade dentro dos grupos:', grausDeLiberdadeDentroDosGrupos)

quadradosMediosEntreGrupos = somaDosQuadradosEntreGrupos / grausDeLiberdadeEntreGrupos
quadradosMediosDentroDosGrupos = somaDosQuadradosDentroDosGrupos / grausDeLiberdadeDentroDosGrupos

print('Quadrados médios entre grupos:', round(quadradosMediosEntreGrupos,2))
print('Quadrados médios dentro dos grupos:', round(quadradosMediosDentroDosGrupos,2))

estatisticaF = quadradosMediosEntreGrupos / quadradosMediosDentroDosGrupos
print('Estatística F:', round(estatisticaF,2))
""" coluna 3 x linha 12 na tabela Z """
fCritico = stats.f.ppf(1 - 0.05, grausDeLiberdadeEntreGrupos, grausDeLiberdadeDentroDosGrupos)

if estatisticaF > fCritico:
    print('Rejeitar a hipótese nula')
else:
    print('Aceitar a hipótese nula')



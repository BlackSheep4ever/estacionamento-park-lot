
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CloudPark.models import Customer, Vehicle, Plan, Contract, Customer_Plan, Contract_Rule, Parkmovement
from CloudPark.serializers import CustomerSerializer, VehicleSerializer, PlanSerializer, ContractSerializer, Customer_PlanSerializer, Contract_RuleSerializer, ParkmovementSerializer

# Create your views here.

# CUSTOMER TABLE API
@csrf_exempt
def customerApi(request, Id=0):
    if request.method=='GET':
        customers = Customer.objects.all()
        customer_Serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_Serializer.data, safe=False)
    elif request.method == 'POST':
        customer_data=JSONParser().parse(request)
        customer_Serializer=CustomerSerializer(data=customer_data)
        if customer_Serializer.is_valid():
            customer_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        customer_data=JSONParser().parse(request)
        customer=Customer.objects.get(Id=customer_data['Id'])
        customer_Serializer=CustomerSerializer(customer, data=customer_data)
        if customer_Serializer.is_valid():
            customer_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        customer_data=JSONParser().parse(request)
        customer=Customer.objects.get(Id=customer_data['Id'])
        customer.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# VEHICLE TABLE API
@csrf_exempt
def vehicleApi(request, Id=0):
    if request.method=='GET':
        vehicles = Vehicle.objects.all()
        vehicle_Serializer = VehicleSerializer(vehicles, many=True)
        return JsonResponse(vehicle_Serializer.data, safe=False)
    elif request.method == 'POST':
        vehicle_data=JSONParser().parse(request)
        vehicle_Serializer=VehicleSerializer(data=vehicle_data)
        if vehicle_Serializer.is_valid():
            vehicle_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        vehicle_data=JSONParser().parse(request)
        vehicle=Vehicle.objects.get(Id=vehicle_data['Id'])
        vehicle_Serializer=VehicleSerializer(vehicle, data=vehicle_data)
        if vehicle_Serializer.is_valid():
            vehicle_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        vehicle_data=JSONParser().parse(request)
        vehicle=Vehicle.objects.get(Id=vehicle_data['Id'])
        vehicle.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# PLAN TABLE API
@csrf_exempt
def planApi(request, Id=0):
    if request.method=='GET':
        plans = Plan.objects.all()
        plan_Serializer = PlanSerializer(plans, many=True)
        return JsonResponse(plan_Serializer.data, safe=False)
    elif request.method == 'POST':
        plan_data=JSONParser().parse(request)
        plan_Serializer=PlanSerializer(data=plan_data)
        if plan_Serializer.is_valid():
            plan_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        plan_data=JSONParser().parse(request)
        plan=Plan.objects.get(Id=plan_data['Id'])
        plan_Serializer=PlanSerializer(plan, data=plan_data)
        if plan_Serializer.is_valid():
            plan_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        plan_data=JSONParser().parse(request)
        plan=Plan.objects.get(Id=plan_data['Id'])
        plan.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# CONTRACT TABLE API
@csrf_exempt
def contractApi(request, Id=0):
    if request.method=='GET':
        contracts = Contract.objects.all()
        contract_Serializer = ContractSerializer(contracts, many=True)
        return JsonResponse(contract_Serializer.data, safe=False)
    elif request.method == 'POST':
        contract_data=JSONParser().parse(request)
        contract_Serializer=ContractSerializer(data=contract_data)
        if contract_Serializer.is_valid():
            contract_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        contract_data=JSONParser().parse(request)
        contract=Contract.objects.get(Id=contract_data['Id'])
        contract_Serializer=ContractSerializer(contract, data=contract_data)
        if contract_Serializer.is_valid():
            contract_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        contract_data=JSONParser().parse(request)
        contract=Contract.objects.get(Id=contract_data['Id'])
        contract.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# CUSTOMER_PLAN TABLE API
@csrf_exempt
def customer_planApi(request, Id=0):
    if request.method=='GET':
        customer_plans = Customer_Plan.objects.all()
        customer_plan_Serializer = Customer_PlanSerializer(customer_plans, many=True)
        return JsonResponse(customer_plan_Serializer.data, safe=False)
    elif request.method == 'POST':
        customer_plan_data=JSONParser().parse(request)
        customer_plan_Serializer=Customer_PlanSerializer(data=customer_plan_data)
        if customer_plan_Serializer.is_valid():
            customer_plan_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        customer_plan_data=JSONParser().parse(request)
        customer_plan=Customer_Plan.objects.get(Id=customer_plan_data['Id'])
        customer_plan_Serializer=Customer_PlanSerializer(customer_plan, data=customer_plan_data)
        if customer_plan_Serializer.is_valid():
            customer_plan_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        customer_plan_data=JSONParser().parse(request)
        customer_plan=Customer_Plan.objects.get(Id=customer_plan_data['Id'])
        customer_plan.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# CONTRACT_RULE TABLE API
@csrf_exempt
def contract_ruleApi(request, Id=0):
    if request.method=='GET':
        contract_rules = Contract_Rule.objects.all()
        contract_rule_Serializer = Contract_RuleSerializer(contract_rules, many=True)
        return JsonResponse(contract_rule_Serializer.data, safe=False)
    elif request.method == 'POST':
        contract_rule_data=JSONParser().parse(request)
        contract_rule_Serializer=Contract_RuleSerializer(data=contract_rule_data)
        if contract_rule_Serializer.is_valid():
            contract_rule_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        contract_rule_data=JSONParser().parse(request)
        contract_rule=Contract_Rule.objects.get(Id=contract_rule_data['Id'])
        contract_rule_Serializer=Contract_RuleSerializer(contract_rule, data=contract_rule_data)
        if contract_rule_Serializer.is_valid():
            contract_rule_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        contract_rule_data=JSONParser().parse(request)
        contract_rule=Contract_Rule.objects.get(Id=contract_rule_data['Id'])
        contract_rule.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
    
# PARKMOVEMENT TABLE API
@csrf_exempt
def parkmovementApi(request, Id=0):
    if request.method=='GET':
        parkmovements = Parkmovement.objects.all()
        parkmovement_Serializer = ParkmovementSerializer(parkmovements, many=True)
        return JsonResponse(parkmovement_Serializer.data, safe=False)
    elif request.method == 'POST':
        parkmovement_data=JSONParser().parse(request)
        parkmovement_Serializer=ParkmovementSerializer(data=parkmovement_data)
        if parkmovement_Serializer.is_valid():
            parkmovement_Serializer.save()
            return JsonResponse("Adicionado com sucesso!", safe=False)
        return JsonResponse("Falha ao adicionar", safe=False)
    elif request.method == 'PUT':
        parkmovement_data=JSONParser().parse(request)
        parkmovement=Parkmovement.objects.get(Id=parkmovement_data['Id'])
        parkmovement_Serializer=ParkmovementSerializer(parkmovement, data=parkmovement_data)
        if parkmovement_Serializer.is_valid():
            parkmovement_Serializer.save()
            return JsonResponse('Dados atualizados!', safe=False)
        return JsonResponse('Falha na atualização!')
    elif request.method == 'DELETE':
        parkmovement_data=JSONParser().parse(request)
        parkmovement=Parkmovement.objects.get(Id=parkmovement_data['Id'])
        parkmovement.delete()
        return JsonResponse('Dado apagado com sucesso!', safe=False)
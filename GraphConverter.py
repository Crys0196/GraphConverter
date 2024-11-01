'''
Author: Crys0196 aircat110@gmail.com
Date: 2024-10-19 11:16:02
LastEditors: Crys0196 aircat110@gmail.com
LastEditTime: 2024-10-19 14:49:11
FilePath: \dot\GraphConverter.py
Description: A function that convert Bayes Tree Graph to BN or MR.

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import pydot
'''
description: If your wanna distinguish x as a child and a parent, change "child=child.strip()"
param {*} BT_file
return {*}
'''
def BT_to_BN(BT_file):
    (graph,)=pydot.graph_from_dot_file(BT_file)
    BN=pydot.Dot("Bayes_Net",graph_type='digraph')
    
    added_nodes = set()
    added_edges = set() 
    
    for node in graph.get_nodes():
        line=node.get_label()
        line=line.strip().strip("\"")
        
        if ':' in line:
            left,right=line.split(':')
            children=left.split(',')
            parents=right.split(',')
            
            for child in children:
                child = child.strip()
                if child not in added_nodes:
                    BN.add_node(pydot.Node(child, label=child))
                    added_nodes.add(child) 
                
                for parent in parents:
                    parent = parent.strip() 
                    if parent not in added_nodes:
                        BN.add_node(pydot.Node(parent, label=parent))
                        added_nodes.add(parent) 
                    edge = (parent, child)  
                    if edge not in added_edges:  
                        BN.add_edge(pydot.Edge(parent, child))
                        added_edges.add(edge)
                    
        else:
            root=pydot.Node("root",label=line)
            BN.add_node(root)
    return BN

def BT_to_MG(BT_file):
    (graph,)=pydot.graph_from_dot_file(BT_file)
    MG=pydot.Dot("Morale_Graph",graph_type='graph')
    
    added_nodes = set()
    added_edges = set()
    
    for node in graph.get_nodes():
        line=node.get_label()
        line=line.strip().strip("\"")
        
        if ':' in line:
            left,right=line.split(':')
            children=left.split(',')
            parents=right.split(',')
            
            for child in children:
                child = child.strip()
                if child not in added_nodes:
                    MG.add_node(pydot.Node(child, label=child))
                    added_nodes.add(child) 
                
                for parent in parents:
                    parent = parent.strip()# 
                    if parent not in added_nodes:
                        MG.add_node(pydot.Node(parent, label=parent))
                        added_nodes.add(parent)
                    
                    edge = (parent, child)  
                    if edge not in added_edges:  
                        MG.add_edge(pydot.Edge(parent, child))
                        added_edges.add(edge)
                    
            for i in range(len(parents)):
                for j in range(i + 1, len(parents)):
                    edge = (parents[i].strip(), parents[j].strip())  
                    if edge not in added_edges and (edge[1], edge[0]) not in added_edges:  
                        MG.add_edge(pydot.Edge(parents[i].strip(), parents[j].strip()))
                        added_edges.add(edge)

        else:
            root=pydot.Node("root",label=line)
            MG.add_node(root)
    return MG

Bayes_Net_Graph=BT_to_BN(".\BT\Bayes_6.000000.dot")

Bayes_Net_Graph.write_dot(".\BN\BN6.dot")

""" if no GraphViz, then do this """  
""" Bayes_Net_Graph.write_raw("BN1.dot") """      

Morale_Graph=BT_to_MG(".\BT\Bayes_6.000000.dot")
Morale_Graph.write_dot(".\MG\MG6.dot")
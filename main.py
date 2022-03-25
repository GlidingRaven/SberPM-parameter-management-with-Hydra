import hydra
import pathlib
import logging
log = logging.getLogger(__name__)
from omegaconf import DictConfig, OmegaConf
import pandas as pd
from sberpm import DataHolder
from sberpm.visual import GraphvizPainter

    
@hydra.main(config_path='conf', config_name='config')
def my_app(cfg : DictConfig) -> None:
#     log.info(OmegaConf.to_yaml(cfg))
    
    def create_dataset():
        full_path = hydra.utils.get_original_cwd() + '\\' + cfg.dataset.filename
        df = pd.read_csv(full_path, cfg.dataset.separator, encoding='latin-1')

        data_holder = DataHolder(data = df, 
                         id_column = cfg.dataset.id_col, 
                         activity_column = cfg.dataset.act_col, 
                         start_timestamp_column = cfg.dataset.time_col, 
                         time_format = cfg.dataset.date_format)
        return data_holder
    
    def mine(dh):
        model_name = cfg.model.name
        
        def make_image(miner):
            miner.apply()
            graph = miner.graph

            painter = GraphvizPainter()
            painter.apply(graph)
            painter.write_graph(model_name + '.' + cfg.out_format, format=cfg.out_format)
            
        
        if model_name == 'simple':
            from sberpm.miners import SimpleMiner
            make_image( SimpleMiner(dh) )
            
        elif model_name == 'casual':
            from sberpm.miners import CausalMiner
            make_image( CausalMiner(dh) )
            
        elif model_name == 'heu':
            from sberpm.miners import HeuMiner
            make_image( HeuMiner(data_holder, threshold=cfg.model.threshold) )
            
        elif model_name == 'alpha':
            from sberpm.miners import AlphaMiner
            make_image( AlphaMiner(dh) )
            
        elif model_name == 'alphaplus':
            from sberpm.miners import AlphaPlusMiner
            make_image( AlphaPlusMiner(dh) )
            
        elif model_name == 'insight':
            from sberpm.miners import SimpleMiner
            from sberpm.autoinsights import AutoInsights
            auto_i = AutoInsights(dh, time_unit='day')
            simple_miner = SimpleMiner(dh)
            
            # Transition duration
            auto_i.apply(miner=simple_miner, mode=cfg.mode)
            graph = auto_i.get_graph()

            painter = GraphvizPainter()
            painter.apply_insights(graph)
            painter.write_graph(model_name + '.' + cfg.out_format, format=cfg.out_format)
            
        else:
            raise ValueError('Model not exist. Check name')
        print('Done')
            
    data_holder = create_dataset()
    mine(data_holder)
                                 

if __name__ == "__main__":
    my_app()
